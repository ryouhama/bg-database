from pydantic import BaseModel, ConfigDict

from app.domain.value_object.base import PrimaryKey


class Entity(BaseModel):
    """
    エンティティの基底クラス
    - id: 主キー
    """

    model_config = ConfigDict(strict=True)
    id: PrimaryKey

    def rebuild(self, params) -> "Entity":
        """
        モデルを再構築する
        """
        return self.__class__(**params)
