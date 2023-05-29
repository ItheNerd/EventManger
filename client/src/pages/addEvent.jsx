import { useAxios } from "@/lib/hooks/hooks";
import { useState } from "react";

const AddEventForm = () => {
  const [eventData, setEventData] = useState({
    event_name: "",
    date: "",
    time: "",
    location: "",
    image: null,
  });

  const api = useAxios();

  const handleChange = (e) => {
    console.log(eventData, typeof e.target.value);
    setEventData({ ...eventData, [e.target.name]: e.target.value });
  };

  const AddEventOnSubmit = async (e) => {
    e.preventDefault();
    api
      .post("/events/create/", eventData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      })
      .then((response) => {
        console.log("Event added successfully:", response);
        setEventData({
          event_name: "",
          date: "",
          time: "",
          location: "",
          image: null,
        });
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  };

  return (
    <form onSubmit={AddEventOnSubmit} encType="multipart/form-data">
      <label>
        Event Name:
        <input
          type="text"
          name="event_name"
          value={eventData.event_name}
          onChange={handleChange}
        />
      </label>
      <br />
      <label>
        Date:
        <input
          type="date"
          name="date"
          value={eventData.date}
          onChange={handleChange}
        />
      </label>
      <br />
      <label>
        Time:
        <input
          type="time"
          name="time"
          value={eventData.time}
          onChange={handleChange}
        />
      </label>
      <br />
      <label>
        Location:
        <input
          type="text"
          name="location"
          value={eventData.location}
          onChange={handleChange}
        />
      </label>
      <br />
      <label>
        Image:
        <input
          type="file"
          name="image"
        //   value={eventData.image}
          //   onChange={handleChange}
          onChange={(e) =>
            setEventData({ ...eventData, [e.target.name]: e.target.files[0] })
          }
          accept="image/jpeg,image/png,image/gif"
        />
      </label>
      <br />
      <button type="submit">Add Event</button>
    </form>
  );
};

export default AddEventForm;
