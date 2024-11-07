// import logo from './logo.svg';
import './App.css';
import './components/TodoItems'
import TodoItems from './components/TodoItems';
function App() {
  // let name = 'MIT';
  
  // function greet(){
  //   alert('Ready!')
  // }
  let todosList = {}
  return (// class is a keywordin js that's why className is used instead of this in react
    <div className="App">
      {/* <p>Hello @K@^ @ {name}</p>
      <button onClick={() => greet()}> Click Me!</button> */}
      <h1>  TO DO</h1>
      

    </div>
  );
}

export default App;
