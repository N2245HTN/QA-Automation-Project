describe('Using Fixtures', () => {

  it('logs in using fixture data', () => {

    cy.fixture('user').then((user) => {

      cy.visit('https://the-internet.herokuapp.com/login')

      cy.get('#username').type(user.username)
      cy.get('#password').type(user.password)

      cy.get('button[type="submit"]').click()

      cy.url().should('include', user.expectedUrl)

    })

  })

})