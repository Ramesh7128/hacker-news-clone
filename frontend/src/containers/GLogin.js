import React, { Component } from 'react';
import { fetchArticles, authLogin, logout } from '../actions/articlesActions';
import { connect } from 'react-redux';
import { Link } from 'react-router-dom'
import { GoogleLogin } from 'react-google-login';
import google from '../img/googlelog.svg'
import axios from 'axios';

class GLogin extends Component {
    constructor(props) {
        super(props);
        this.googleResponse = this.googleResponse.bind(this);
    }

    onFailure = (error) => {
        alert(error);
    };

    googleResponse = (response) => {
        console.log(response);
        const options = {
            access_token: response.accessToken,
        };
        axios.post('http://127.0.0.1:8000/social/google-oauth2/', options).then(r => {
            if (r.data.token) {
                this.props.loggedIn(r.data.token, response.profileObj.imageUrl, response.profileObj.name);
            }
        });
    };

    render() {
        if (this.props.token) {
            return (
                <div className='profile-section'>
                    <div>
                        <img className='profile-pic' src={this.props.imgUrl} alt='UserImg' />
                    </div>
                    <div>
                        <span>Logout</span>
                    </div>
                </div>
            )
        } else {
            return (
                <div>
                    <GoogleLogin
                        clientId="705813183307-hminde5i1ejhm790gl6t2ct0j6n7vft0.apps.googleusercontent.com" //CLIENTID NOT CREATED YET
                        render={renderProps => (
                            <button className='btnGoogle' onClick={renderProps.onClick}><img src={google} alt='google' /><span>Login</span></button>
                        )}
                        buttonText="LOGIN"
                        onSuccess={this.googleResponse}
                        onFailure={this.onFailure}
                        className='btnGoogle'
                    />
                </div>
            )
        }
    }
}


const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        loggedIn: (token, imgUrl, fullName) => dispatch(authLogin(token, imgUrl, fullName)),
    }
}

const mapStateToProps = (state) => {
    return {
        token: state.user,
        imgUrl: state.imgUrl,
        fullName: state.fullName
    }
}

GLogin = connect(mapStateToProps, mapDispatchToProps)(GLogin);
export default GLogin