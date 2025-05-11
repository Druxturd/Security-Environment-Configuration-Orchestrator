from PyQt5.QtCore import QAbstractItemModel, QModelIndex, Qt, QVariant

class TreeItem:
    def __init__(self, data, parent=None):
        self.parentItem = parent
        self.itemData = data
        self.childItems = []
    
    def appendChild(self, child):
        self.childItems.append(child)
    
    def child(self, row):
        return self.childItems[row]

    def childCount(self):
        return len(self.childItems)
    
    def row(self):
        if self.parentItem:
            return self.parentItem.childItems.index(self)
        return 0

    def data(self):
        return self.itemData
    
    def parent(self):
        return self.parentItem
    
class DetailReportModel(QAbstractItemModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.rootItem = TreeItem("Root")
        self.setupModelData(data)

    def setupModelData(self, data):
        for target in data:
            targetLbl = f"{target.host} - {target.ip}"
            targetItem = TreeItem({"type": "target", "label": targetLbl, "details": target}, self.rootItem)
            self.rootItem.appendChild(targetItem)

            for playbook in target.playbook_results:
                pbItem = TreeItem({"type": "playbook", "label": playbook.name, "details": playbook}, targetItem)
                targetItem.appendChild(pbItem)

    def columnCount(self, parent=QModelIndex()):
        return 1
    
    def rowCount(self, parent=QModelIndex()):
        if not parent.isValid():
            return self.rootItem.childCount()
        parentItem = parent.internalPointer()
        return parentItem.childCount()
    
    def index(self, row, column, parent=QModelIndex()):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()
        if not parent.isValid():
            parentItem = self.rootItem
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
        if parentItem == self.rootItem:
            return QModelIndex()
        return self.createIndex(parentItem.row(), 0, parentItem)
    
    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return QVariant()
        item = index.internalPointer()
        if role == Qt.ItemDataRole.DisplayRole:
            return item.data()['label']
        return QVariant()