import React, { Component } from 'react';
import { Link, Redirect } from 'react-router-dom';
import { authSignUp, authLogout } from '../actions/articlesActions';
import { connect } from 'react-redux';


class SignupForm extends Component {
    constructor(props) {
        super(props);
        this.state = {
            username: '',
            email: '',
            password: ''            
        }
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleInput =  this.handleInput.bind(this);
    }

    componentDidMount() {
        this.props.logoutAuth();
    }

    handleSubmit(event) {
        event.preventDefault();
        this.props.signUpAuth(this.state.email, this.state.username, this.state.password);
    }

    handleInput(event) {
        let key = event.target.name;
        let value = event.target.value;
        let newState = {};
        newState[key] = value;
        this.setState(newState);
    }
    render() {
        let errorMsg = []
        for (let key in this.props.authError) {
            errorMsg.push(this.props.authError[key][0]); 
        }
        if (this.props.isAuthenticated) return <Redirect to="/" />;
        return (
            <div className='login-box-container'>
                <div className='login-title'>Signup</div>
                <div className="login-item">
                    <form onSubmit={this.handleSubmit} className="form form-login">
                        {errorMsg.map((item)=><p className='error-msg'>*{item}</p>)}
                        <div className="form-field">
                            <label className="user" htmlFor="login-username"><span className="hidden">Email</span></label>
                            <input
                                type="text"
                                name="email"
                                placeholder='Email'
                                onChange={this.handleInput}
                            />
                        </div>
                        <div className="form-field">
                            <label className="user" htmlFor="login-username"><span className="hidden">Username</span></label>
                            <input
                                type="text"
                                name="username"
                                placeholder='Username'
                                onChange={this.handleInput}
                            />
                        </div>
                        <div className="form-field">
                        <label className="lock" htmlFor="login-password"><span className="hidden">Password</span></label>
                            <input
                                type="password"
                                name="password"
                                placeholder='password'
                                onChange={this.handleInput}
                            />
                        </div>
                        <div className="form-field">
                            <input
                                type="submit"
                                value="REGISTER"
                                onSubmit={this.handleSubmit}
                            />
                        </div>
                    </form>
                </div>
                <Link to="/login"><div className='signup-link'>Login</div></Link>
            </div>
        );
    }
}

const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        signUpAuth : (email, username, password) => dispatch(authSignUp(email, username, password)),
        logoutAuth: () => dispatch(authLogout())
    }
}

const mapstateToProps = (state) => {
    return {
        authError: state.authError,
        isAuthenticated: state.isAuthenticated,
    }
}

SignupForm = connect(mapstateToProps, mapDispatchToProps)(SignupForm);
export default SignupForm;
