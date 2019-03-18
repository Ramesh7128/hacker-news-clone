import { combineReducers } from "redux";

import {
    FETCH_STORIES_BEGIN,
    FETCH_STORIES_SUCCESS,
    FETCH_STORIES_FAILURE,
    FETCH_SEARCH_STORIES_BEGIN,
    FETCH_SEARCH_STORIES_SUCCESS,
    FETCH_SEARCH_STORIES_FAILURE,
    CONTENT_PAGE_RERENDER,
    AUTH_START,
    AUTH_SUCCESS,
    AUTH_FAIL,
    AUTH_LOGOUT,
} from '../actions/articlesActions';

const token = localStorage.getItem('token');
const imgUrl = localStorage.getItem('imgUrl');
const fullName = localStorage.getItem('fullName');

const initialState = {
    token: null,
    username: null,
    isAuthenticated: false,
    authLoading: false,
    imgUrl: null,
    authError: null,
    articles: [],
    reRender: false,
    prevLink: null,
    error: null,
    nextLink: null,
    startIndex: null,
    endIndex: null,
    articleCount: 0,
    searchArticles: [],
    fetching: false,
    fetched: false,
}


function reducer(state = initialState, action) {
    switch (action.type) {
        case FETCH_STORIES_BEGIN:
            return {
                ...state,
                fetching: true,
            }
        case FETCH_STORIES_SUCCESS:
            return {
                ...state,
                fetched: true,
                fetching: false,
                error: '',
                articles: action.payload.data,
                prevLink: action.payload.prevlink,
                nextLink: action.payload.nextlink,
                startIndex: action.payload.startIndex,
                endIndex: action.payload.endIndex,
                articleCount: action.payload.count,
                searchArticles: [],

            }
        case FETCH_STORIES_FAILURE:
            return {
                ...state,
                fetching: false,
                error: action.payload,
            }
        case FETCH_SEARCH_STORIES_BEGIN:
            return {
                ...state,
                fetching: true,
            }
        case FETCH_SEARCH_STORIES_SUCCESS:
            return {
                ...state,
                error: '',
                fetched: true,
                fetching: false,
                articles: action.payload.data,
            }
        case FETCH_SEARCH_STORIES_FAILURE:
            return {
                ...state,
                fetching: false,
                error: action.payload
            }
        case AUTH_START:
            return {
                ...state,
                isAuthenticated: false,
                authError: null,
                authLoading: true
            }
        case AUTH_SUCCESS:
            return {
                ...state,
                token: action.token,
                username: action.username,
                isAuthenticated: true,
                authError: null,
                authLoading: false
            }
        case AUTH_FAIL:
            return {
                ...state,
                isAuthenticated: false,
                authError: action.error,
                authLoading: false
            }
        case AUTH_LOGOUT:
            return {
                ...state,
                token: null,
                isAuthenticated: false,
                authLoading: false,
                authError: null
            }
        case CONTENT_PAGE_RERENDER:
            return {
                ...state,
                reRender: true
            }
        default:
            return state;
    }
}

export default reducer;