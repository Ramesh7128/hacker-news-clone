import React, { Component } from 'react';
import { connect } from 'react-redux';
// import search from './img/search.svg';
import { fetchArticles, fetchSearchArticles } from '../actions/articlesActions';

class Search extends Component {
    constructor(props) {
        super(props);
        // this.handleInputText = this.handleInputText.bind(this);
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
                    <input className='input-box' type="text" onChange={(event) => this.props.onChange(event.target.value)} placeholder="Search" />
                </span>
            </div>
        )
    }
}

const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        onChange: (query) => {
            console.log(query);
            if (query) {
                dispatch(fetchSearchArticles(query));
            } else {
                dispatch(fetchArticles('/api/topstories/'));
            }
        }
    }
}

Search = connect(null, mapDispatchToProps)(Search);
export default Search