import React, { Component } from 'react';
import { connect } from 'react-redux';
import Sentiment from '../components/Sentiment';
import thumbsUp from '../img/thumbsup.svg';
import { starArticles } from '../actions/articlesActions';


class Story extends Component {
    constructor(props) {
        super(props);
        this.state = {
            checkbox: this.props.article.is_checked
        }
        this.handleSelect = this.handleSelect.bind(this);
    }

    handleSelect(event) {
        starArticles(event.target.dataset.id);
        this.setState(prevState => ({
            checkbox: !prevState.checkbox
        }));
    }
    render() {
        let link = this.props.article.link;
        let concatLink = '';
        if (link.length > 17) {
            concatLink = link.slice(0, 17) + "...";
        } else {
            concatLink = link;
        }
        let passedSeconds = Math.floor(Date.now() / 1000) - this.props.article.timestamp;
        let hours = Math.floor(passedSeconds / 3600);
        let minutes = Math.floor((passedSeconds % 3600) / 60);
        return (
            <div className='story-box'>
                <div className='list-numbering story-item'>
                    <div className="number-text">
                        {this.props.idx + this.props.startIndex}
                    </div>
                </div>
                <div className='title-section story-item'>
                    <a href={this.props.article.link} target="_blank" rel="noopener noreferrer">
                        <div className="title-text">
                            <div>
                                {this.props.article.title}
                            </div>
                            <div className='title-author'>
                                {this.props.article.author} - {hours ? hours + " hours ago" : minutes + " minutes ago"} - ({concatLink})
                            </div>
                        </div>
                    </a>
                </div>
                <div className='score-section story-item'>
                    <div className='score-text'>
                        <img className='score-icon' src={thumbsUp} alt="icon" />
                        {this.props.article.score}
                    </div>
                </div>
                <div className='sentiment-section story-item'>
                    <Sentiment score={this.props.article.sentiment_score} />
                </div>
                {this.props.isAuthenticated &&
                    <div className="story-item">
                        <input onClick={this.handleSelect} data-id={this.props.articleID} type="checkbox" checked={this.state.checkbox}/>
                    </div>
                }
            </div>
        )
    }
}

const mapStateToProps = state => ({
    isAuthenticated: state.isAuthenticated,
    token: state.token
})

Story = connect(mapStateToProps)(Story);
export default Story