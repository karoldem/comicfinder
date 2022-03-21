const base = {"http://smbc-comics.com": "  \n\n \n\n \n  \n\nYOU KNOW HOW YOU SIT ON THE COUCH,\nEATING SNACKS, USING A CONTROLLER TO\nRUN AROUND A FANTASY WORLD?\n\n \n    \n \n  \n \n\n  \n\nWHAT IF IT WAS\nTHE SAME THING,\nBUT YOU HAD\nTO STAND?\n\n \n     \n \n\n \n\n \n\nI will never understand the idea of a metaverse.\n\f", "https://www.smbc-comics.com/comic/clouds-3": "DO YOU SEE ANYTHING IN THAT ONE LOOKS TO ME LIKE\n\nTHE CLOUDS? A LONNNNG PATHWAY AND AT\nTHE FAR END THERES A LADY\nWITH A SAD FACE LOOKING\nBACK OVER THE PATH\n\n \n\f", "https://www.smbc-comics.com/comic/reviews": "YOU ARE GREAT AT IT\nT HAVE TO TELL YOU ALL OF\nMY FAVORITE PARTS SO LET\nME PULL UP MY NOTES/\n\n       \n      \n  \n\nLIFE TIP:\n\nYOU CAN TELL.\nHOW BAD YOU ARE\nAT SOMETHING BY\n\nHOW UNFOCUSED\nTHE CONSTRUCTIVE\nCRITICISM IS\n\n \n\nYOU ARE DECENT\n\nTHIS IS REALLY NICE WORK\nOVERALL, BUT I HAVE SOME,\nTHOUGHTS. LIKE HERE\nIN CHAPTER 3...\n\n     \n     \n     \n\n  \n   \n     \n\nYOU KNOW IT WAS AN\nINTERESTING EXPERIENCE.\nREADING THE WORDS\nYOU WROTE.\n\n  \n\n \n\naYOUR BOOK? GOOD? BAD,\nWHAT ARE WE? IS ANY OF\nTHIS EVEN REAL?\n\n \n\f"}

export default {
  data() {
    return {
      xkcd: true,
      smbc:true,
      search:'',
      result:{},
      sortedResult: null
    }
  },

  methods:{
    send(event){
      if (event !== ''){
        this.result = {}
        for (const [key, value] of Object.entries(base)) {

          var matchExists = false;

          this.search.split(' ').forEach((element) => {

            if (value.includes(element.toUpperCase())){
              if (matchExists) { this.result[key] +=1; }
              else {
                matchExists = true;
                this.result[key] = 1;
              }

            }
          });
        }

        var items = Object.keys(this.result).map(
          (key) => { return [key, this.result[key]] });

        items.sort(
          (first, second) => { return first[1] - second[1] }
        ).reverse();
        this.result = items;

      }
    }
  }
}
