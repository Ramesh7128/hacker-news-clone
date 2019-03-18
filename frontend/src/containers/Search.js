import React, { Component } from 'react';
import { connect } from 'react-redux';
// import search from './img/search.svg';
import { fetchArticles, fetchSearchArticles } from '../actions/articlesActions';
import google from '../img/google.png'

class Search extends Component {
    constructor(props) {
        super(props);
    }

    handleInputText(event) {
        console.log(event.target.value)

    }
    handleItemMapping() {
    }
    handleRenderMapping() {
    }
    toggleOpen() {
        const openCheck = !this.state.openCheck;
        this.setState(state => ({
            openCheck: openCheck
        }));
    }
    render() {
        return (
            <div className='search-section'>
                <span className="input-section">
                    <input className='input-box' type="text" onChange={(event) => this.props.onChange(event.target.value, this.props.token)} placeholder="Search" />
                </span>
            </div>
        )
    }
}

const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        onChange: (query, token) => {
            console.log(query);
            if (query) {
                dispatch(fetchSearchArticles(query, token));
            } else {
                dispatch(fetchArticles('/api/topstories/', token));
            }
        }
    }
}

const mapStateToProps = (state) => ({
    token: state.user,
});

Search = connect(mapStateToProps, mapDispatchToProps)(Search);
export default Search