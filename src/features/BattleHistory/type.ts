/**
 * ヒーロー
 * バトルグラウンドで選択したヒーロー
 */
export type Hero = {
  id: number
  name: string
  img: string
  effect: string
}

/**
 * 異常
 * バトルグラウンドで適応された異常
 */
export type Anomaly = {
  id: number
  name: string
  img: string
  effect: string
}

/**
 * バトル履歴
 * バトルグラウンドにおける1回の戦闘履歴
 */
export type BattleHistory = {
  id: number
  date: Date
  hero: Hero
  anomaly: Anomaly
  rate: number
}

