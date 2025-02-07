function generateRenderJson(text1, text2, video) {
    return {
        templateId: 'dd01cee7-d517-4148-aa32-7f91130bf6b1',
        modifications: {
            'Text-1': text1,
            'Text-2': text2,
            'video': video
        }
    };
}

// Usage
const renderJson = generateRenderJson('Hi!, Thanks for trying Creatomate','Welcome to Distinct software company !','https://videos.pexels.com/video-files/2887463/2887463-hd_1920_1080_25fps.mp4'
);

const creatomate = require('creatomate');
const client = new creatomate.Client('708f398635974958b3bf6aec0e531d92f71ac76a99e160573100e833d3473f2d3fc669e0b9a7f9d502eae04af854dc07');

console.log("Please wait while your video is being rendered....!");
client.render(renderJson).then((renders) => {
    console.log('Completed', renders);
});
