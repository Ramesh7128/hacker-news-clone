import React, { Component } from 'react';
import arrow from '../img/arrow.svg'
import { fetchArticles } from '../actions/articlesActions';
import { connect } from 'react-redux';


class Footer extends Component {
    render() {
        console.log(this.props.token);
        return (
            <div className='pagination'>
                { this.props.nextLink && 
                    <img onClick={() => this.props.onClick(this.props.nextLink)} src={arrow} alt="" />
                }
            </div>
        )
    }
}

const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        onClick: (nextLink) => dispatch(fetchArticles(nextLink))
    }
}

const mapStateToProps = (state) => ({
    nextLink: state.nextLink,
    token: state.user
})

Footer = connect(mapStateToProps, mapDispatchToProps)(Footer);
export default Footer