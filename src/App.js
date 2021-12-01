import './App.css';
import axios from 'axios';
import { Grid, Button, TextField, MenuItem, Select, InputLabel, FormControl, Typography, Alert } from '@mui/material';
import { useState } from 'react';



const App = ()  => {
  const [type, setType] = useState('');
  const [ip, setIp] = useState('');
  const [port, setPort] = useState('');
  const [packets, setPackets] = useState(null);
  const [success, setSuccess] = useState(false);
  const [sending, setSending] = useState(false);
  const CallAPI = async() => {
    setSuccess(false)
    setSending(true)
    var response = await axios.get(`/${type}?ip=${ip}&pktCount=${packets}&port=${port}`)
    if(response.data === "Success"){
      setSuccess(true);
    }
    setSending(false)
  }

  return (
    <div className="App">
        <Grid container style = {{width: '50%', padding: '40px'}} spacing = {2}>
          <Grid item xs = {12}>
            <Typography fullWidth variant = 'h3' style = {{fontWeight: 'lighter'}}>DDos Attacker</Typography>
          </Grid>
          {(sending) ? 
            <Grid item xs = {12}>
              <Alert style = {{width: '100%', padding: 0}} severity="info">DDoS attack is being sent...</Alert>
            </Grid>
            : null}
          {(success) ? 
            <Grid item xs = {12}>
              <Alert style = {{width: '100%', padding: 0}} severity="success">DDos attack was successfull</Alert>
            </Grid>
            : null}
          <Grid item xs = {6}>
            <FormControl fullWidth>

              <InputLabel id="demo-simple-select-standard-label">Attack Type</InputLabel>

              <Select
                style = {{width: '100%'}}
                label = "Attack Type"
                onChange = {(e) => setType(e.target.value)}
              >
                <MenuItem value = 'udp'>UDP</MenuItem>
                <MenuItem value = 'icmp'>ICMP</MenuItem> 
                <MenuItem value = 'tcp'>TCP</MenuItem> 

              </Select>
            </FormControl>

          </Grid>
          <Grid item xs = {6}>
            <TextField 
              style = {{width: '100%'}} 
              placeholder = "Ip Address"
              onChange = {(e) => setIp(e.target.value)}
            />
          </Grid>
          <Grid item xs = {4}>
            <TextField  
              style = {{width: '100%'}}  
              placeholder = "Port"
              onChange = {(e) => setPort(e.target.value)}
            />
          </Grid>
          <Grid item xs = {4}>
            <TextField 
              style = {{width: '100%'}} 
              placeholder = "Packets"
              onChange = {(e) => setPackets(e.target.value)}
            />
          </Grid>
          <Grid item xs = {4}>
            <Button 
              fullWidth 
              style = {{height: '100%', backgroundColor: '#1976d2', color: 'white'}}
              onClick = {() => CallAPI()}
            >
              Send
            </Button>
          </Grid>
        </Grid>
        {/* <Button styles = {{color: 'white'}} onClick = {() => CallAPI()}>Click</Button> */}
    </div>
  );
}

export default App;
