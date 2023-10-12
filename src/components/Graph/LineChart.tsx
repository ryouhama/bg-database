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

export const LineChartFrame: React.FC<PropsWithChildren<Props>> = (props) => {
  const { width, height, dataset, children } = props

  const dataWithConverted = convertDatasetToLineChartData(dataset)

  return (
    <LineChart
      width={width || undefined}
      height={height || undefined}
      data={dataWithConverted}
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
    name: `2023-10-${it.x}`,
    [title]: it.y
  }))
}
