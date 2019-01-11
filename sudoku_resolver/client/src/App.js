import React, { Component } from 'react';
import logo from './logo.svg';
import Sudoku, {Cell} from './components/sudokuMatrix';
import './App.css';

class App extends Component {

  constructor(props) {
    super(props);
    this.state = {
      message : "Click on SOLVE button to solve the SUDOKU",
      status : "Unsolved",
      size : 9,
      data : [[3,0,6,5,0,8,4,0,0], 
              [5,2,0,0,0,0,0,0,0], 
              [0,8,7,0,0,0,0,3,1], 
              [0,0,3,0,1,0,0,8,0], 
              [9,0,0,8,6,3,0,0,5], 
              [0,5,0,0,9,0,6,0,0], 
              [1,3,0,0,0,0,2,5,0], 
              [0,0,0,0,0,0,0,7,4], 
              [0,0,5,2,0,6,3,0,0]],
    }
    this.handleChange = this.handleChange.bind(this);
    this.onSubmit = this.onSubmit.bind(this);
    this.handleDataChange = this.handleDataChange.bind(this);
  }
  

  handleDataChange(pos, e) {
    let matrix = [...this.state.data]
    let value = parseInt(e.target.value)
    matrix[pos[0]][pos[1]] = value ? value>9 ? 0 : value : 0 ;
    this.setState((state, props)=>({ data: [...matrix] }));
  }

  onSubmit() {
     fetch('http://localhost:5000/api/v1/solution?data='+JSON.stringify(this.state.data))
      .then(response => {
        console.log(response.body)
        return response.json()
      })
      .then(data => {
        this.setState((state, props)=>({ data: data.data, status: data.message }))
      }).
      catch(function(error) {
        console.log('Looks like there was a problem: \n', error);
      });
  }

  handleChange = (pos, e) => {
    e.persist();
    if(e.target.value!==""){
      let value = parseInt(e.target.value);
      if(value<=12){
        this.setState((state, props)=>({
          size : value,
        }))
      } else {
        console.log("size is very big");
      }
    
    }    
  }
  
  render() {
    return (
      <div className="App">    
        <div> {this.state.message} </div> 
        <div> 
          <span>{"STATUS : "}</span>
          {this.state.status} 
        </div>
        <Sudoku
          size = {this.state.size}
          data = {this.state.data}
          handleChange = {this.handleDataChange}
          value = {"SOLVE"}
        />
        <div>
          <input
            type="submit" 
            name="name" 
            onSubmit={ this.onSubmit }
            onClick={ this.onSubmit }
          />
        </div> 
      </div>
    );
  }
}

export default App;
