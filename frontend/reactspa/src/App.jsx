// import logo from './logo.svg';
import './App.css';
import './components/TodoItems'
import TodoItems from './components/TodoItems';
function App() {
  // let name = 'MIT';
  
  // function greet(){
  //   alert('Ready!')
  // }

  return (// class is a keywordin js that's why className is used instead of this in react
    <div className="App">
      {/* <p>Hello @K@^ @ {name}</p>
      <button onClick={() => greet()}> Click Me!</button> */}
      <h1>  TO DO</h1>
      <br /><br />
      <h2>Wake Up</h2>
      <p>Time : 6:00 A.M.</p>
      <p>Completed</p>
      <TodoItems title="Lunch" desc="12:35 P.M." status="Pending"/>
      <TodoItems title="Elite" desc="05:30 P.M." status="Started"/>
    </div>
  );
}

export default App;
