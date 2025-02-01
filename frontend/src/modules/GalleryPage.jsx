function GalleryPage(){
    const images = [
        {
            filepath: '/src/assets/cat-dog-couch.jpg',
            caption: 'My dog Milo and my cat Luna playing on the couch.',
            title: '&copy; 2024 Roman Depyak'
        },
        {
            filepath: '/src/assets/fantasy-cave-bermuda-stalactites-brackish-water.jpg',
            caption: 'A photo I took of Fantasy Cave in Bermuda.',
            title: '&copy; 2024 Roman Depyak'
        },
        {
            filepath: '/src/assets/graph-python-output-comparing-bubble-insertion-sort.png',
            caption: 'Graph comparing Bubble Sort and Insertion Sort performance.',
            title: '&copy; 2024 Roman Depyak'
        },
        {
            filepath: '/src/assets/hashmap-put-function.png',
            caption: 'HashMap put function implementation.',
            title: '&copy; 2024 Roman Depyak'
        },
        {
            filepath: '/src/assets/library_simulator_return_item_funtion.png',
            caption: 'Library simulator: Return item function.',
            title: '&copy; 2024 Roman Depyak'
        }
    ];

    return (
        <>
            <h2>Gallery</h2>
            <p>
                This gallery includes photos from previous coding projects, photos from my previous travels, and a photo of my pets.
            </p>
            <article className="gallery">
                {images.map((image, index) => (
                    <figure key={index}>
                        <img src={image.filepath} alt={image.caption} title={image.title} />
                        <figcaption>{image.caption}</figcaption>
                    </figure>
                ))}
            </article>
        </>
    );
}

export default GalleryPage;