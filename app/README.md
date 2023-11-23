# Application Directory
- domain: ドメイン層
  - entity: エンティティが配置される
  - value_object: バリューオブジェクトが配置される
  - repository_interface: ドメインを操作するリポジトリーのインターフェイスが配置される
- application: アプリケーション層
  - usecase: 業務ロジックに関するユースケース処置が配置される
- infrastructure: インフラストラクチャ層
  - controller: APIのエンドポイントとなるコントローラーが配置される
  - db: DB操作に関する処理が配置される
  - repository: リポジトリーインターフェイスの実体クラスが配置される

