import React, { Component } from 'react';
// import search from './img/search.svg';
import FuzzyPicker from 'react-fuzzy-picker';

class Search extends Component {
    constructor(props) {
        super(props);
        // this.state = {
        //     openCheck: false,
        // }
        // this.handleSelect = this.handleSelect.bind(this);
        // this.toggleOpen = this.toggleOpen.bind(this);
        // this.handleItemMapping = this.handleItemMapping.bind(this);
        // this.handleRenderMapping = this.handleRenderMapping.bind(this);
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
        return (
            <div className='search-section'>
                <span class="input">
                    <input type="text" placeholder="Search" />
                </span>
            </div>
        )
    }
}

export default Search