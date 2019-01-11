import React, {Fragment} from 'react';
import ReactDOM from 'react-dom';


export const Cell = (props) => {
	const {
		placeholder, position, handleChange, style, value
	} = props

	const css = style ? style :{
		height: "50px",
		width: "50px",
		textAlign: "center"
	}
	
	return (
		<Fragment>
			<input
				type="text" 
				name="name" 
				style={css} 
				onChange={ (e)=>handleChange(position ? position : 0, e) }
				value={value}
			/>
		</Fragment>
	)
}


export default (props) => {
	let size = props.size;
	let matrix = props.data ? props.data : [...Array(size).keys()].map(()=>[...Array(size).keys()])

	return (
		<Fragment>
			<div>
				{matrix.map((row, outerValue)=>{
					return (
						<div key={outerValue}>
							{row.map((value, innerValue)=>{
								return (
										<Cell 
											key = {innerValue}
											position = {[outerValue, innerValue]}
											value = {value}
											handleChange = {props.handleChange}
										/>
									)
							})}
						</div>
					)
				})}
			</div>
		</Fragment>
	)
}