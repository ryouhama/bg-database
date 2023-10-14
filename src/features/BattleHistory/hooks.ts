import { type BattleHistory, type Hero, type Anomaly } from './type'
import { add, addDays } from 'date-fns'

const dammyMasterHerosData: Hero[] = [
  {
    id: 1,
    name: "A.F.ケイ",
    img: "",
    effect: ""
  }
]

const dammyMasterAnomalyData: Anomaly[] = [
  {
    id: 1,
    name: "",
    img: "",
    effect: ""
  }
]

const today = new Date()
const dammy: BattleHistory[] = [0, 0, 0, 0, 0].map((_, index) => ({
  id: index,
  date: addDays(today, index),
  hero: dammyMasterHerosData[0],
  anomaly: dammyMasterAnomalyData[0],
  rate: 8000 + index
}))

/**
 * バトルグラウンドの戦闘履歴に関するhooks
 * @returns 
 */
export const useUserBattleHistory = () => {
  const battleHistories: BattleHistory[] = dammy

  const edit = (id: number, date: Date, hero: Hero, anomaly: Anomaly, rate: number) => {
    // TODO: 更新処理
    return {
      id: id,
      date: date,
      hero: hero,
      anomaly: anomaly,
      rate: rate
    }
  }
  
  const add = (date: Date, hero: Hero, anomaly: Anomaly, rate: number) => {
    const nextId = Math.max(...battleHistories.map((it) => it.id)) + 1
    return {
      id: nextId,
      date: date,
      hero: hero,
      anomaly: anomaly,
      rate: rate
    }
  }
 
  const deleteHistory = (id: number) => {
    console.log(`削除対象 id=${id}`)
  }

  return {
    /** 対象ユーザーのバトルグラウンドの戦歴一覧 */
    battleHistories,
    /** 追加 */
    add,
    /** 更新 */
    edit,
    /** 削除 */
    deleteHistory
  }
}


/**
 * バトルグラウンドのマスタデータに関するhooks
 * @return {{ heros: Hero[], anomalies: Anomaly[] }}
 *  - heros: ヒーローマスタ
 *  - anomalies: 異常マスタ
 */
export const useBattleGroundMaster = () => {
  // TODO: 後で取得処理を実装する
  // 一旦ダミーデータで代用
  const heros: Hero[] = dammyMasterHerosData
  const anomalies: Anomaly[] = dammyMasterAnomalyData
  return {
    heros,
    anomalies
  }
}
