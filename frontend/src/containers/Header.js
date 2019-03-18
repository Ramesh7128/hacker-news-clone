import React, { Component } from 'react';
import { fetchArticles } from '../actions/articlesActions';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom'

class Header extends Component {

    constructor(props) {
        super(props);
    }

    render() {

        return (
            <div className='header-section'>
                <div onClick={() => this.props.onClickTop(this.props.token)} className='logo-box'>Y</div>
                <div className='top-articles' onClick={() => this.props.onClickTop()}>
                    <span role="img" aria-label="top">🔥</span>
                    <Link to="/category/toparticles">Top Posts</Link>
                </div>
                <div className='top-articles' onClick={() => this.props.onClickNew()}>
                    <span role="img" aria-label="top">🔥</span>
                    <Link to="/category/newarticles">New Posts</Link>
                </div>
                {
                    this.props.isAuthenticated &&
                    <div className='top-articles' onClick={() => this.props.onClickStarred()}>
                        <span role="img" aria-label="top">🔥</span>
                        <Link to="/category/starred">Starred</Link>
                    </div>
                }
            </div>
        )

    }
}


const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        onClickTop: () => dispatch(fetchArticles('/api/topstories/')),
        onClickNew: () => dispatch(fetchArticles('/api/newstories/')),
        onClickStarred: () => dispatch(fetchArticles('/api/starred/'))
    }
}

const mapStateToProps = (state) => ({
    isAuthenticated: state.isAuthenticated,
    articles: state.articles,
    prevLink: state.prevLink,
    nextLink: state.nextLink,
    searchArticles: state.searchArticles,
    startIndex: state.startIndex,
    fetching: state.fetching,
    fetched: state.fetched,
    error: state.error,
    token: state.token,
});

Header = connect(mapStateToProps, mapDispatchToProps)(Header);
export default Header