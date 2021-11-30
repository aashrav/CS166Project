import './App.css';
import axios from 'axios';
import {Button} from '@mui/material'

async function CallAPI(){
  var response = await axios.get('/udp_flood')
  console.log(response)
}

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Button styles = {{color: 'white'}} onClick = {() => CallAPI()}>Click</Button>
      </header>
    </div>
  );
}

export default App;
