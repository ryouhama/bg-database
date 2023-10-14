import { LineChart, CartesianGrid, YAxis, XAxis, Tooltip, Legend, Line } from 'recharts'
import { useUserBattleHistoryLineChart } from "./hooks"

export const BattleHistoryLineChart = () => {
  const { dataset } = useUserBattleHistoryLineChart()

  return (
    <LineChart
      width={730}
      height={250}
      data={dataset}
      // TODO: marginなどのスタイルは外から渡せる様にする
      margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
    >
      <CartesianGrid />
      <XAxis dataKey="name" />
      <YAxis type="number" domain={['dataMin - 500', 'dataMax + 500']}/>
      <YAxis/>
      <Tooltip />
      <Legend />
      <Line type="monotone" dataKey="rate" stroke="#8884d8" />
    </LineChart>
  )
}