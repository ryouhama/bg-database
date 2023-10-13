import { type DataSet } from './components/Graph'
import { Home } from './pages/Home';

const generateRandomArray = () => {
  const min = 8000;
  const max = 10000;
  const arrayLength = 10;
  const randomArray = [Math.floor(Math.random() * (max - min + 1)) + min];

  for (let i = 1; i < arrayLength; i++) {
    const previousValue = randomArray[i - 1];
    // Generate a random number in the range [-50, 50]
    const randomOffset = Math.floor(Math.random() * 101) - 50;
    const newValue = previousValue + randomOffset;

    // Ensure the generated value stays within the [min, max] range
    randomArray.push(Math.max(min, Math.min(max, newValue)));
  }

  return randomArray;
}

export const App = () => {
  const width = 730
  const height = 250
  const dataset: DataSet = {
    title: "hoge",
    data: generateRandomArray().map((it, index) => ({x: index, y: it}))
  } 
  return <Home/>
}
