import React from 'react'

function TodoItems(props) {
  console.log(props);// JS Object File : Props - Not KeyWord but Good Practice
  let title=props.title || "default title";
  let desc=props.desc;
  let status=props.status;
  let time=props.created_at
  return (
    <div className='TodoItem'>
      <h2>{title}</h2>
      <p>{desc}</p>
      <p>{status}</p>
      <p>Created At:{time}</p>
    </div>
  )
}

export default TodoItems