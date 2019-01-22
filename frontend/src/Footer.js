import React, { Component } from 'react';
import arrow from './img/arrow.svg'

class Footer extends Component {
    render() {
        return (
            <div className='footer-section'>
                <img onClick={this.props.handleMoreArticlesClick} src={arrow} alt=""/>
            </div>
        )
    }
}

export default Footer