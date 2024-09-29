// import { Font } from "lib-font";
import { Font } from "./lib-font-browser.js";

const myFont = new Font(`Inter`);

// Assign event handling (.addEventListener version supported too, of course)
myFont.onerror = (evt) => console.error(evt);
myFont.onload = (evt) => doSomeFontThings(evt);

// Kick off the font load by setting a source file, exactly as you would
// for an <img> or <script> element when building them as nodes in JS.
// myFont.src = `./InterVariable.ttf`;
myFont.src = `./NotoSansSC-VF.ttf`;


// When the font's up and loaded in, let's do some testing!
function doSomeFontThings(evt) {
  // We can either rely on scoped access to font, but because the onload function
  // is not guaranteed to live in the same scope, the font is in the event, too.
  const f = evt.detail.font;

  const font = f.reverse(13383)
  console.log(font)

  // First, let's test some characters:
  // [`a`, `→`, `嬉`].forEach((char) =>
  //   console.log(`Font supports '${char}': ${f.supports(char)}`)
  // );

  // Then, let's check some OpenType things
  const GSUB = f.opentype.tables.GSUB;

  // Let's figure out which writing scripts this font supports:
  console.log(
    `This font supports the following scripts: ${`"${GSUB.getSupportedScripts().join(
      `", "`
    )}"`}`
  );

  // DFLT is a given, but let's see if `latn` has any special language/system rules...
  const latn = GSUB.getScriptTable("latn");
  console.log(
    `Special langsys for "latn": ${`"${GSUB.getSupportedLangSys(latn).join(
      `", "`
    )}"`}`
  );

  // // Wow, "Northern Sami" support? Really? Which OpenType features does that use?
  // const nsm = GSUB.getLangSysTable(latn, "NSM ");
  // console.log(
  //   `OpenType features for the Northern Sami version of latin script:`,
  //   `"${GSUB.getFeatures(nsm)
  //     .map((f) => f.featureTag)
  //     .join(`", "`)}"`
  // );

  // Oh wait, this is a variable font, isn't it.
  console.log(`This is a variable font: ${!!f.opentype.tables.fvar}`);

  // Which axes does it support?
  console.log(
    `This variable font supposed the following axes: ${`"${f.opentype.tables.fvar
      .getSupportedAxes()
      .join(`", "`)}"`}`
  );
}
