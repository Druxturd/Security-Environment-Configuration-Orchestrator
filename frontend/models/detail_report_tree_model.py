from PySide6.QtCore import (
    QAbstractItemModel,
    QModelIndex,
    Qt,
    QMetaType
)

class TreeItem:
    def __init__(self, data, parent=None):
        self.parent_item = parent
        self.item_data = data
        self.child_items = []
    
    def append_child(self, child):
        self.child_items.append(child)
    
    def child(self, row):
        return self.child_items[row]

    def child_count(self):
        return len(self.child_items)
    
    def row(self):
        if self.parent_item:
            return self.parent_item.child_items.index(self)
        return 0

    def data(self):
        return self.item_data
    
    def parent(self):
        return self.parent_item
    
class DetailReportModel(QAbstractItemModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.root_item = TreeItem("Root")
        self.setup_model_data(data)

    def setup_model_data(self, data):
        for target in data:
            targetLbl = f"{target.host} - {target.ip}"
            target_item = TreeItem({"type": "target", "label": targetLbl, "details": target}, self.root_item)
            self.root_item.append_child(target_item)

            for playbook in target.playbook_results:
                playbook_item = TreeItem({"type": "playbook", "label": playbook.name, "details": playbook}, target_item)
                target_item.append_child(playbook_item)

    def columnCount(self, parent=QModelIndex()):
        return 1
    
    def rowCount(self, parent=QModelIndex()):
        if not parent.isValid():
            return self.root_item.child_count()
        parentItem = parent.internalPointer()
        return parentItem.child_count()
    
    def index(self, row, column, parent=QModelIndex()):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()
        if not parent.isValid():
            parentItem = self.root_item
        else:
            parentItem = parent.internalPointer()
        childItem = parentItem.child(row)
        if childItem:
            return self.createIndex(row, column, childItem)
        return QModelIndex()
    
    def parent(self, index):
        if not index.isValid():
            return QModelIndex()
        childItem = index.internalPointer()
        parentItem = childItem.parent()
        if parentItem == self.root_item:
            return QModelIndex()
        return self.createIndex(parentItem.row(), 0, parentItem)

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return QMetaType()
        item = index.internalPointer()
        if role == Qt.ItemDataRole.DisplayRole:
            return item.data()['label']
        return QMetaType()