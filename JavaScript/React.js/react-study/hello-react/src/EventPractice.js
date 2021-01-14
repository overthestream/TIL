import React, { Component } from "react"

class EventPractice extends Component {
	state = {
		message: "",
		username: "",
	}
	handleChange = (e) => {
		this.setState({
			[e.target.name]: e.target.value,
		})
	}
	handleClick = () => {
		alert(this.state.username + " : " + this.state.message)
		this.setState({
			message: "",
			username: "",
		})
	}
	render() {
		return (
			<div>
				<h1>이벤트 연습</h1>
				<input
					type="text"
					name="username"
					placeholder="username"
					value={this.state.username}
					onChange={this.handleChange}
				/>
				<input
					type="text"
					name="message"
					placeholder="enter anything"
					value={this.state.message}
					onChange={this.handleChange}
				/>
				<button onClick={this.handleClick}>OK</button>
			</div>
		)
	}
}

export default EventPractice
