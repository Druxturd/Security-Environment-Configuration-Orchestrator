from PySide6.QtCore import QAbstractItemModel, QModelIndex, Qt


class TreeItem:
    def __init__(self, data, parent=None):
        self._data = data
        self._parent = parent
        self._children = []

    def appendChild(self, item):
        self._children.append(item)

    def child(self, row):
        return self._children[row] if 0 <= row < len(self._children) else None

    def childCount(self):
        return len(self._children)

    def data(self):
        return self._data

    def parent(self):
        return self._parent

    def row(self):
        if self._parent:
            return self._parent._children.index(self)
        return 0


class DetailReportModel(QAbstractItemModel):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self._root_item = TreeItem({"type": "root"})
        self.setup_model_data(data)

    def setup_model_data(self, data):
        for target in data:
            host_name = f"{target.host} - {target.ip}"
            host_item = TreeItem({"type": "host", "name": host_name}, self._root_item)
            self._root_item.appendChild(host_item)

            for playbook in target.playbook_results:
                playbook_item = TreeItem(
                    {"type": "playbook", "name": playbook.name, "details": playbook},
                    host_item,
                )
                host_item.appendChild(playbook_item)

    def index(self, row, column, parent=QModelIndex()):
        if not self.hasIndex(row, column, parent):
            return QModelIndex()

        parent_item = (
            self._root_item if not parent.isValid() else parent.internalPointer()
        )
        child_item = parent_item.child(row)

        if child_item:
            return self.createIndex(row, column, child_item)
        return QModelIndex()

    def parent(self, index):
        if not index.isValid():
            return QModelIndex()

        child_item = index.internalPointer()
        parent_item = child_item.parent()

        if parent_item == self._root_item or parent_item is None:
            return QModelIndex()

        return self.createIndex(parent_item.row(), 0, parent_item)

    def rowCount(self, parent=QModelIndex()):
        parent_item = (
            self._root_item if not parent.isValid() else parent.internalPointer()
        )
        return parent_item.childCount()

    def columnCount(self, parent=QModelIndex()):
        return 1

    def data(self, index, role=Qt.ItemDataRole.DisplayRole):
        if not index.isValid():
            return None

        item = index.internalPointer()
        if role == Qt.ItemDataRole.DisplayRole:
            return item.data().get("name", "")
        return None

    def flags(self, index):
        if not index.isValid():
            return Qt.ItemFlag.NoItemFlags
        return Qt.ItemFlag.ItemIsEnabled | Qt.ItemFlag.ItemIsSelectable
