import React, { Component } from 'react';
import sad from '../img/sad.svg';
import meh from '../img/confused.svg';
import happy from '../img/happy.svg';


class Sentiment extends Component {
    render() {
        if (!this.props.score) {
            return <img src={meh} alt='neutral'/>
            
        }
        if (this.props.score > 0) {
            return <img src={happy} alt='happy'/>
        } else {
            return <img src={sad} alt='sad'/>
        } 
    }
}

export default Sentiment