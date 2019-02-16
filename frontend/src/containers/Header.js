import React, { Component } from 'react';
import { fetchArticles } from '../actions/articlesActions';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom'

class Header extends Component {

    render() {
        return (
            <div className='header-section'>
                <div onClick={this.props.onClick} className='logo-box'>Y</div>
                <div className='top-articles' onClick={this.props.onClickTop}>
                    <span role="img" aria-label="top">🔥</span>
                    <Link to="/toparticles">Top Posts</Link>
                </div>
                <div className='top-articles' onClick={this.props.onClickNew}>
                    <span role="img" aria-label="top">🔥</span>
                    <Link to="/newarticles">New Posts</Link>
                </div>
            </div>
        )
    }
}

const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        onClickTop: () => dispatch(fetchArticles('/api/topstories/')),
        onClickNew: () => dispatch(fetchArticles('/api/newstories/'))
    }
}

Header = connect(null, mapDispatchToProps)(Header);
export default Header