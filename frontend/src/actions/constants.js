// development setup
export const baseUrl = 'http://127.0.0.1:8000';
// production setup
// export const baseUrl = window.location.origin;


export const authLoginURL =  baseUrl + '/api/users/login';
export const authSignUPURL =  baseUrl + '/api/users/';
export const tokenAuthenticationURL = baseUrl + '/api/user';
export const starredArticlesURL = baseUrl + '/api/starred';

