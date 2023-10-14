import { useUserBattleHistory } from "../hooks"
import { format } from 'date-fns'

export const useUserBattleHistoryLineChart = () => {
  const { battleHistories } = useUserBattleHistory()

  const dataset = battleHistories.map((battleHistory) => ({
    name: format(battleHistory.date, "yyyy-MM-dd hh-mm-ss"),
    rate: battleHistory.rate
  }))

  return {
    dataset
  }
}
