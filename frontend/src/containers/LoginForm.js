import React, { Component } from 'react';
import { Link, Redirect } from 'react-router-dom'
import { authLogin, authLogout } from '../actions/articlesActions';
import { connect } from 'react-redux';

class LoginForm extends Component {
    constructor(props) {
        super(props);
        this.state = {
            'email': '',
            'password': ''
        };
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleInput = this.handleInput.bind(this);
    }

    componentDidMount() {
        this.props.LogoutAuth();
    }

    handleSubmit = event => {
        event.preventDefault();
        this.props.LoginAuth(this.state.email, this.state.password);
    }

    handleInput(event) {
        let key = event.target.name;
        let value = event.target.value;
        let newState = {};
        newState[key] = value;
        this.setState(newState);
    }

    render() {
        let errorMsg = ''
        for (let key in this.props.authError) {
            errorMsg += this.props.authError[key];
        }
        if (this.props.isAuthenticated) return <Redirect to="/" />;
        return (
            <div className='login-box-container'>
                <div className='login-title'>Login</div>
                <div className="login-item">
                    <form onSubmit={this.handleSubmit} className="form form-login">
                        <p className='error-msg'>{errorMsg}</p>
                        <div className="form-field">
                            <label className="user" htmlFor="login-email"><span className="hidden">EmailID</span></label>
                            <input
                                type="text"
                                name="email"
                                placeholder='email'
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
                                value="LOG IN"
                                onSubmit={this.handleSubmit}
                            />
                        </div>
                    </form>
                </div>
                <Link to="/signup"><div className='signup-link'>Signup</div></Link>
            </div>
        );
    }
}

const mapDispatchToProps = (dispatch, ownProps) => {
    return {
        LoginAuth: (email, password) => dispatch(authLogin(email, password)),
        LogoutAuth: () => dispatch(authLogout())
    }
}

const mapstateToProps = (state) => {
    return {
        authError: state.authError,
        isAuthenticated: state.isAuthenticated,
        authLoading: state.authLoading
    }
}

LoginForm = connect(mapstateToProps, mapDispatchToProps)(LoginForm);
export default LoginForm;