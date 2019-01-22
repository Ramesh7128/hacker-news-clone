import React, { Component } from 'react';

class Header extends Component {
    render() {
        return (
            <div className='header-section'>
                <div onClick={this.props.handleTopArticleClick} className='logo-box'>Y</div>
                <div className='top-articles' onClick={this.props.handleTopArticleClick}><span role="img" aria-label="top">🔥</span> Top Posts</div>
            </div>
        )
    }
}

export default Header