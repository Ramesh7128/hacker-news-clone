import React, { Component } from 'react';
import { connect } from 'react-redux';
import { fetchArticles, fetchSearchArticles } from '../actions/articlesActions';
import GLogin from './GLogin';
import Login from './Login';

class Nav extends Component {
    constructor(props) {
        super(props);
    }
    render() {

        return (
            <div className='nav-section'>
                <span className="input-section">
                    <input className='input-box' type="text" onChange={(event) => this.props.onChange(event.target.value)} placeholder="Search" />
                </span>
                {/* <GLogin /> */}
                <Login />
            </div>
          );
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

// const mapStateToProps = (state) => {
//     return {
//         isAuthenticated: state.isAuthenticated
//     }
// }

Nav = connect(null, mapDispatchToProps)(Nav);
export default Nav;
