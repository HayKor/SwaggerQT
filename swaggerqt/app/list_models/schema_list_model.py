from PyQt6.QtCore import QAbstractListModel, QModelIndex, Qt


class SchemaListModel(QAbstractListModel):
    def __init__(self, schemas: list[str] = []) -> None:
        super().__init__()
        self.schemas: list[str] = schemas or []

    def data(self, index: QModelIndex, role: int = ...):
        if role == Qt.ItemDataRole.DisplayRole:
            return self.schemas[index.row()]  # Show the name in the list

    def rowCount(self, parent: QModelIndex = ...):
        return len(self.schemas)

    def get_schema(self, index: QModelIndex):
        if index.isValid():
            return self.schemas[index.row()]
        return None

    def add_schema(self, schema: str):
        self.beginInsertRows(
            QModelIndex(), len(self.schemas), len(self.schemas)
        )
        self.schemas.append(schema)
        self.endInsertRows()

    def remove_schema(self, index: QModelIndex):
        if index.isValid():
            self.beginRemoveRows(QModelIndex(), index.row(), index.row())
            self.schemas.pop(index.row())
            self.endRemoveRows()