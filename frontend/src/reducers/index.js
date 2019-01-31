import {
    FETCH_PRODUCTS_BEGIN,
    FETCH_PRODUCTS_SUCCESS,
    FETCH_PRODUCTS_FAILURE
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


function reducer(state=initialState, action) {
    switch (action.type) {
        case FETCH_PRODUCTS_BEGIN:
            return {
                ...state,
                fetching: true,
            }
        case FETCH_PRODUCTS_SUCCESS:
            return {
                ...state,
                fetched: true,
                fetching: false,
                articles: action.payload.data,
                prevLink: action.payload.prevlink,
                nextLink: action.payload.nextlink,
                startIndex: action.payload.startIndex,
                endIndex: action.payload.endIndex,
                articleCount: action.payload.count,
                searchArticles: [],

            }
        case FETCH_PRODUCTS_FAILURE:
            return {
                ...state,
                fetching: false,
                error: action.payload,
            }
        default:
            return state;
    }
}

export default reducer;