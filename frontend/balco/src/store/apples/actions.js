/*
export function someAction (context) {
}
*/
export function addData ({ commit }, payload) {
  commit('setApples', payload.total)
  commit('setK', payload.K)
  commit('setL', payload.L)
}
