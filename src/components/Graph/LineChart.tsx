import { PropsWithChildren } from 'react'
import { LineChart, CartesianGrid, YAxis, XAxis, Tooltip, Legend, Line } from 'recharts'

type Props = {
  width: number | null
  height: number | null
  dataset: DataSet
}

export type Data = {
  x: number
  y: number
}
export type DataSet = {
  title: string
  data: Data[]
}

// TODO: `xxFrame`みたいな感じになってしまい、本来のComponentからズレてる
// 理想は、component -> パーツ、features -> 機能
// 機能寄りの内容が多いため、featuresに移行する。Recharts自体が豊富に機能を提供しているため、ラップしたものは作らない様にしたい
// ただし、型は作りたし
export const LineChartFrame: React.FC<PropsWithChildren<Props>> = (props) => {
  const { width, height, dataset, children } = props

  const dataWithConverted = convertDatasetToLineChartData(dataset)

  return (
    <LineChart
      width={width || undefined}
      height={height || undefined}
      data={dataWithConverted}
      // TODO: marginなどのスタイルは外から渡せる様にする
      margin={{ top: 5, right: 30, left: 20, bottom: 5 }}
    >
      <CartesianGrid />
      <YAxis type="number" domain={['dataMin - 500', 'dataMax + 500']}/>
      <XAxis dataKey="name" />
      <Tooltip />
      <Legend />
      <Line type="monotone" dataKey={dataset.title} stroke="#8884d8" />
      {children}
    </LineChart>
  )
}

const convertDatasetToLineChartData = (dataset: DataSet) => {
  const title = dataset.title
  return dataset.data.map((it) => ({
    // TODO: x軸は入力されたデータを加工せず参照する
    name: `2023-10-${it.x}`,
    [title]: it.y
  }))
}
