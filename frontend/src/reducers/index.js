import { combineReducers } from "redux";

import {
    FETCH_STORIES_BEGIN,
    FETCH_STORIES_SUCCESS,
    FETCH_STORIES_FAILURE,
    FETCH_SEARCH_STORIES_BEGIN,
    FETCH_SEARCH_STORIES_SUCCESS,
    FETCH_SEARCH_STORIES_FAILURE
} from '../actions/articlesActions';

const initialState = {
    articles: [],
    prevLink: '',
    error: '',
    nextLink: '',
    startIndex: '',
    endIndex: '',
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
        default:
            return state;
    }
}

export default reducer;