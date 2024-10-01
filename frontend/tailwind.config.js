module.exports = {
  purge: ["./src/**/*.{js,jsx,ts,tsx}"],
  darkMode: false,
  theme: {
    extend: {
      screens: {
        desktop: { min: "1320px" },
        tablet: { min: "641px", max: "1321px" },
        mobile: { max: "640px" },
      },
    },
  },
  variants: {},
  plugins: [],
};
