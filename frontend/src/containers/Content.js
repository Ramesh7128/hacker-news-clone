import React, { Component } from 'react';
import Story from '../components/Story';
import { connect } from 'react-redux';
import { fetchArticles } from '../actions/articlesActions';

class Content extends Component {
    componentDidMount() {
        this.props.dispatch(fetchArticles('/api/topstories/'));
    }
    render() {
        if (this.props.searchArticles.length) {
            if (this.props.fetching) {
                return <div className='content-section'>Loading...</div>
            } else {
                return (
                    <div className='content-section'>
                        {this.props.searchArticles.map((article, idx) => (
                            <Story startIndex={1} key={article.id} article={article} idx={idx} />
                        ))}
                    </div>
                )
            }
        } else {
            if (this.props.fetching) {
                return <div className='content-section'>Loading...</div>
            } else {
                if (this.props.error) {
                    return <div className='content-section'>{this.props.error.message}</div>
                } else {
                    return (
                        <div className='content-section'>
                            {this.props.articles.map((article, idx) => (
                                <Story startIndex={this.props.startIndex} key={article.id} article={article} idx={idx} />
                            ))}
                        </div>
                    )
                }
            }
        }
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
    error: state.error
});

Content = connect(mapStateToProps)(Content);
export default Content