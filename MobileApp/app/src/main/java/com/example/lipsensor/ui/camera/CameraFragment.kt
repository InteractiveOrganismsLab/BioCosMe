package com.example.lipsensor.ui.camera

import android.os.Bundle
import android.view.LayoutInflater
import android.view.View
import android.view.ViewGroup
import android.widget.TextView
import androidx.fragment.app.Fragment
import androidx.lifecycle.ViewModelProvider
import com.example.lipsensor.databinding.FragmentCameraBinding
import androidx.navigation.fragment.findNavController
import com.example.lipsensor.R


class CameraFragment : Fragment() {

    private var _binding: FragmentCameraBinding? = null

    // This property is only valid between onCreateView and
    // onDestroyView.
    private val binding get() = _binding!!

    override fun onCreateView(
        inflater: LayoutInflater,
        container: ViewGroup?,
        savedInstanceState: Bundle?
    ): View {
        val cameraViewModel =
            ViewModelProvider(this).get(CameraViewModel::class.java)

        _binding = FragmentCameraBinding.inflate(inflater, container, false)
        val root: View = binding.root

        val textView: TextView = binding.textCamera
        cameraViewModel.text.observe(viewLifecycleOwner) {
            textView.text = it
        }
        return root
    }

    override fun onViewCreated(view: View, savedInstanceState: Bundle?) {
        super.onViewCreated(view, savedInstanceState)

        // Set click listener for the button to navigate to the GalleryFragment
        binding.btnOpenGallery.setOnClickListener {
            // Navigate to the GalleryFragment using the NavController
            findNavController().navigate(R.id.action_nav_camera_to_nav_gallery)
        }
    }


    override fun onDestroyView() {
        super.onDestroyView()
        _binding = null
    }

}