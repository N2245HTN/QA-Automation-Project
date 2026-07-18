describe("Login UI Test", () => {
  beforeEach(() => {
    cy.visit("https://www.saucedemo.com/");
  });

  it("logs in with valid credentials", () => {
    cy.get("#user-name").type("standard_user");
    cy.get("#password").type("secret_sauce");
    cy.get("#login-button").click();

    cy.url().should("include", "/inventory.html");
    cy.get(".inventory_list").should("be.visible");
  });

  it("shows error for invalid login", () => {
    cy.get("#user-name").type("wrong");
    cy.get("#password").type("wrong");
    cy.get("#login-button").click();

    cy.get('[data-test="error"]')
      .should("be.visible")
      .and("contain", "Username and password do not match");
  });
});
