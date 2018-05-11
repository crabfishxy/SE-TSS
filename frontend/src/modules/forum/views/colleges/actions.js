import {DEBUG, ROOT_URL} from "../../configs/config"

export const GET_COLLEGES = 'get_colleges';
export const GOT_COLLEGES = 'got_colleges';

export const getColleges = () => {
    return (dispatch) => {
        fetchColleges()
            .then((data) => {
                dispatch({
                    type: GOT_COLLEGES,
                    colleges: data
                })
            })
    }
};

function fetchColleges() {
    return fetch(`${ROOT_URL}/api/forum/colleges`)
        .then((response) => (response.json()))
}
