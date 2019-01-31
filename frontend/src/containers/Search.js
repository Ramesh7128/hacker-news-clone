import React, { Component } from 'react';
import search from './img/search.svg';
import FuzzyPicker from 'react-fuzzy-picker';

class Search extends Component {
    constructor(props) {
        super(props);
        this.state = {
            openCheck: false,
        }
        this.handleSelect = this.handleSelect.bind(this);
        this.toggleOpen = this.toggleOpen.bind(this);
        this.handleItemMapping = this.handleItemMapping.bind(this);
        this.handleRenderMapping = this.handleRenderMapping.bind(this);
    }

    handleSelect(choice) {
        const openCheck = !this.state.openCheck;
        this.props.handleArticleSearch(choice);
        this.setState(state => ({
            openCheck: openCheck
        }));
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
        const openCheck = this.state.openCheck;
        console.log(openCheck);
        const list = this.props.articles.map((article) => article.title);
        return (
            <div className='search-section'>
                <FuzzyPicker
                    label='Search for Titles'
                    isOpen={this.state.openCheck}
                    displayCount={6}
                    autoCloseOnEnter={true}
                    onClose={this.toggleOpen}
                    onChange={this.handleSelect}
                    items={list}
                />
                <img className='search-icon' onClick={this.toggleOpen} src={search} alt='search icon'></img>
            </div>
        )
    }
}

export default Search