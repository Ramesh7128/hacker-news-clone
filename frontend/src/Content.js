import React, { Component } from 'react';
import Story from './Story'

class Content extends Component {
    render() {
        if (this.props.article.searchArticles.length) {
            if (!this.props.article.isLoaded) {
                return <div className='content-section'>Loading...</div>    
            } else {
                return (
                    <div className='content-section'>
                        {this.props.article.searchArticles.map((article,idx) => (
                            <Story startIndex={1} key={article.id} article={article} idx={idx}/>
                        ))}
                    </div>
                )
            }
        } else {
            if (!this.props.article.isLoaded) {
                return <div className='content-section'>Loading...</div>    
            } else {
                return (
                    <div className='content-section'>
                        {this.props.article.articles.map((article,idx) => (
                            <Story startIndex={this.props.article.startIndex} key={article.id} article={article} idx={idx}/>
                        ))}
                    </div>
                )
            }
        }
    }
}

export default Content