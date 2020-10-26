import Vue from 'vue'
import SOAMashup from '@/components/SOAMashup'

describe('SOAMashup.vue', () => {
  it('should render correct contents', () => {
    const Constructor = Vue.extend(SOAMashup)
    const vm = new Constructor().$mount()
    expect(vm.$el.querySelector('.hello h1').textContent)
      .toEqual('Welcome to Your Vue.js App')
  })
})
