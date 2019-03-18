import React, { Component } from 'react';
import Story from './Story';
import { connect } from 'react-redux';
import { fetchArticles } from '../actions/articlesActions';
import Footer from './Footer';

class Content extends Component {
    constructor(props) {
        super(props);
    }
    componentDidMount() {
        console.log(this.props);
        if ('match' in this.props) {
            if ('id' in this.props.match.params) {
                if (this.props.match.params.id === "toparticles") {
                    this.props.dispatch(fetchArticles('/api/topstories/', this.props.user));
                } else if (this.props.match.params.id === "newarticles") {
                    this.props.dispatch(fetchArticles('/api/newstories/', this.props.user));
                }
            } else {
                this.props.dispatch(fetchArticles('/api/topstories/', this.props.user));    
            }
        } else {
            this.props.dispatch(fetchArticles('/api/topstories/', this.props.user));
        }
    }
    render() {
            if (!this.props.fetched) {
                return <div className='content-section'>Loading...</div>
            } else {
                if (this.props.error) {
                    return <div className='content-section'>{this.props.error.message}</div>
                } else {
                    return (
                        <div className='content-section'>
                            {this.props.articles.map((article, idx) => (
                                <Story startIndex={this.props.startIndex} articleID={article.id} key={article.id} article={article} idx={idx} />
                            ))}
                            <Footer />
                        </div>
                    )
                }
            }
        // }
    }
}

const mapStateToProps = (state) => ({
    articles: state.articles,
    prevLink: state.prevLink,
    nextLink: state.nextLink,
    searchArticles: state.searchArticles,
    startIndex: state.startIndex,
    fetching: state.fetching,
    fetched: state.fetched,
    error: state.error,
    token: state.user,
    reRender: state.reRender,
});

Content = connect(mapStateToProps)(Content);
export default Content